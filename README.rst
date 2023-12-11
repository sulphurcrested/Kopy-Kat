Kopy-Kat
========
kopy-kat is a scrapy spider that crawls a website and copy it's content!

Settings
--------
Before setting Kopy-Kat, you need to install **[Scapy](https://docs.scrapy.org/en/latest/)**:
``pip install Scrapy``


The kopy-kat spider is called ``kopy-kat.py`` and is located under ``kopy-kat/spiders``.
At the top of the class modify the ``custom_settings`` object to point to a base url and
a base content path::

        custom_settings = {
                "KOPY-KAT_BASE_URL": "https://github.com/sulphurcrested/Kopy-Kat",
                "KOPY-KAT_BASE_CONTENT_PATH": "./content/",
                "KOPY-KAT_SAVE_FILE": True,
                "KOPY-KAT_MAX_CRAWLS": -1
            }

The Kopy-Kat Config:
    * ``KOPY-KAT_BASE_URL``: the website url to be copied by Kopy-Kat. Kopy-Kat will not copy any content
        that **does not** start with this URL.
    * ``KOPY-KAT_BASE_CONTENT_PATH``: the local path where to save the copied content. The content will be
        structured in different directories as refrenced by website structure.
    * ``KOPY-KAT_SAVE_FILE``: usually ``True`` to save the content or set it to ``False`` to play with Kopy-Kat!
    * ``KOPY-KAT_MAX_CRAWLS``: the maximum number of links to crawl (and copy). If it is set to less than or 
        equal to zero then Kopy-Kat will crawl (and copy) the entire site.

Running Kopy-Kat
----------------
from the main project directory, run:
``scrapy crawl kopy-kat``