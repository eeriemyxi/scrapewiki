# Scrapewiki - Wikipedia Scraper

It can scrape [Wikipedia](http://wikipedia.org) synchronously and asynchronously.
[`scrapewiki.Scrapewiki`](https://github.com/m-y-x-i/scrapewiki/blob/master/scrapewiki/core.py#L8-L16) has two methods, `search` and `wiki`.

### `wiki`
It is used to scrape a Wikipedia page.

### `search`
It is used to search some query on Wikipedia. `limit` parameter can be optionally specified to set a limit to the amount of results.

## Examples
Asynchronous:

```python
import scrapewiki
import trio


wiki = scrapewiki.Scrapewiki()


async def main():
    async with wiki.search("python") as results:
        async for search_result in results:
            ...

    # equivalent of

    searcher = wiki.search("python")
    results = await searcher.async_method()

trio.run(main)
```
```python
import scrapewiki
import trio


wiki = scrapewiki.Scrapewiki()


async def main():
    async with wiki.wiki("python", limit=45) as page:
        ...

    # equivalent of

    page_scraper = wiki.wiki("python")
    page = await page_scraper.async_method()

trio.run(main)
```
Synchronous:

```python
import scrapewiki


wiki = scrapewiki.Scrapewiki()


with wiki.search("python", limit=45) as results:
    for search_result in results:
        ...

# equivalent of

searcher = wiki.search("python")
results = searcher.sync_method()
```
```python
import scrapewiki


wiki = scrapewiki.Scrapewiki()


with wiki.wiki("python") as page:
    ...

# equivalent of

page_scraper = wiki.wiki("python")
page = page_scraper.sync_method()
```

### Extras
The module also provides some utility functions for ease of use (currently just one):
- [`scrapewiki.util.convert_bytes_to`](https://github.com/m-y-x-i/scrapewiki/blob/master/scrapewiki/util/converters.py#L6-L13)

#### Plans
There are a lot of things that needs to be parsed.
There are a lot of bugs that needs to be fixed.
I'm pretty sure there are some typos in docstrings and wrong annotations as well.
My plan for now is to fix the aforesaid problems.

### Note
This library is English only due to how some things have been parsed. I'm sure there are better ways to do them and make it support all languages. This is in my TODO list.

### Documentation
I don't have any plans for online documentation as of now. Please read the source code. All the dataclasses can be found [here.](https://github.com/m-y-x-i/scrapewiki/blob/master/scrapewiki/structures/dataclasses.py)
