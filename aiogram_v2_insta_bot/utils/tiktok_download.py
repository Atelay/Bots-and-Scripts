async def download(url, session):
    request_url = f'https://api.douyin.wtf/api?url={url}'
    async with session.get(request_url) as response:
        data = await response.json()
        video = data['video_data']['nwm_video_url_HQ']
        desc = data["desc"]
        author = f'@{data["author"]["unique_id"]}'
        return [video, author, desc]
