import pprint
import time

import trio

import scrapewiki

wiki = scrapewiki.Scrapewiki()

EACH_ITEM_TIME = 0.3
EACH_TEST_CASE_TIME = 2
count = 1


async def main():
    print("TESTING SYNC WIKI SEARCH SCRAPING")
    time.sleep(EACH_TEST_CASE_TIME)
    with wiki.search("python") as result:
        for index, page in enumerate(result):
            print(f"ITEM NUMBER: {index + 1}")

            for k, v in vars(page).items():
                print(f"{k.upper()}:")
                pprint.pprint(v)

            print("SHOWING NEXT ITEM")
            time.sleep(EACH_ITEM_TIME)

    print("TESTING SYNC WIKI PAGE SCRAPING")
    time.sleep(EACH_TEST_CASE_TIME)
    with wiki.wiki("python") as page:
        for k, v in vars(page).items():
            print(f"{k.upper()}:")
            pprint.pprint(v)
            time.sleep(EACH_ITEM_TIME)

    print("TESTING ASYNC WIKI SEARCH SCRAPING")
    time.sleep(EACH_TEST_CASE_TIME)
    async with wiki.search("python") as result:
        index = 1
        async for page in result:
            print(f"ITEM NUMBER: {index}")

            for k, v in vars(page).items():
                print(f"{k.upper()}:")
                pprint.pprint(v)

            print("SHOWING NEXT ITEM")
            index += 1
            time.sleep(EACH_ITEM_TIME)

    print("TESTING ASYNC WIKI PAGE SCRAPING")
    time.sleep(EACH_TEST_CASE_TIME)
    async with wiki.wiki("List_of_snakes_by_common_name") as page:
        for k, v in vars(page).items():
            print(f"{k.upper()}:")
            pprint.pprint(v)
            time.sleep(EACH_ITEM_TIME)

    print("TESTING WIKIPY.UTILS.CONVERT_BYTES_TO")
    time.sleep(EACH_TEST_CASE_TIME)
    async with wiki.search("python") as result:
        index = 1
        async for page in result:
            print(f"ITEM NUMBER: {index}")

            for name, value in scrapewiki.structures.BytesConvertUnits._member_map_.items():
                print(f"CONVERTING BYTES TO {name}")
                print(scrapewiki.util.convert_bytes_to(value, page.size))

            print("SHOWING NEXT ITEM")
            index += 1
            time.sleep(EACH_ITEM_TIME)

    print("TESTING 300 RESULTS")
    time.sleep(EACH_TEST_CASE_TIME)
    async with trio.open_nursery() as nursery:
        async with wiki.search("python", 300) as result:
            async for page in result:
                nursery.start_soon(
                    await_and_print,
                    wiki.wiki(page.title).async_method,
                    page,
                    globals()["count"],
                )
                globals()["count"] += 1


async def await_and_print(func, page, count):
    try:
        returned = await func()
        print(f"{count} - {returned.title} - DONE")
    except Exception as e:
        print(f"failed at {page.title}")
        raise e


trio.run(main)
