from aiohttp import ClientSession
import asyncio


async def get_items(session: ClientSession, url: str, discount: int) -> list[dict]:
    async with session.get(url) as response:
        data: dict = await response.json()
        items = data.get("items")
        result = []
        for i in items:
            if i["pricing"]["discount"] is not None and i["pricing"][
                "discount"
            ] >= float(f"0.{discount}"):
                item_name = i["asset"]["names"]["full"]
                try:
                    item_3d = i["links"]["3d"]
                except:
                    item_3d = None
                item_price = f'{i["pricing"]["computed"]} $'
                item_discount = f'{round(i["pricing"]["discount"]*100, 2)} %'
                result.append(
                    {
                        "item_name": item_name,
                        "item_3d": item_3d,
                        "item_discount": item_discount,
                        "item_price": item_price,
                    }
                )
        return result


async def csgo_parser(
    category: int = 2, discount: int = 10, min: int = 2000, max: int = 10_000
) -> list[dict]:
    result = []
    offset = 0
    step_size = 60
    async with ClientSession() as session:
        tasks = []
        while True:
            for item in range(offset, offset + step_size, 60):
                url = f"https://cs.money/1.0/market/sell-orders?limit=60&minPrice={min}&maxPrice={max}&sort=discount&offset={item}&type={category}"
                task = asyncio.create_task(get_items(session, url, discount))
                tasks.append(task)
                offset += step_size
            if not tasks:
                break
            items = await asyncio.gather(*tasks)
            for i in items:
                result += i
            tasks = []
            if len(items) < 60:
                break
    return result
