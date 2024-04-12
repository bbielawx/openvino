import xml.etree.ElementTree as ET
import queue
from pathlib import Path
<<<<<<< HEAD
from sphinx_sitemap import setup as base_setup, get_locales, hreflang_formatter, add_html_link, record_builder_type
from sphinx.util.logging import getLogger
=======
from sphinx_sitemap import setup as base_setup, get_locales, hreflang_formatter
>>>>>>> ba86d7460e (new bulild changes)

logger = getLogger(__name__)

def setup(app):
    app.add_config_value(
        'ov_sitemap_urlset',
        default=None,
        rebuild=''
    )
    
    app.add_config_value(
        'ov_sitemap_meta',
        default=None,
        rebuild=''
    )

    setup = base_setup(app)
    for listener in app.events.listeners['build-finished']:
        if listener.handler.__name__ == 'create_sitemap':
            app.disconnect(listener.id)
        
    app.connect("builder-inited", record_builder_type)
    app.connect("html-page-context", add_html_link)
    app.connect('build-finished', create_sitemap)
    return setup


def create_sitemap(app, exception):
    """Generates the sitemap.xml from the collected HTML page links"""

    urlset = app.builder.config.ov_sitemap_urlset
    meta = app.builder.config.ov_sitemap_meta

    site_url = app.builder.config.site_url or app.builder.config.html_baseurl
<<<<<<< HEAD
    if site_url:
        site_url.rstrip("/") + "/"
    else:
        logger.warning(
            "sphinx-sitemap: html_baseurl is required in conf.py." "Sitemap not built.",
            type="sitemap",
            subtype="configuration",
        )
=======
    site_url = site_url.rstrip('/') + '/'
    if not site_url:
        print("sphinx-sitemap error: neither html_baseurl nor site_url "
              "are set in conf.py. Sitemap not built.")
>>>>>>> ba86d7460e (new bulild changes)
        return
    if (not app.sitemap_links):
        print("sphinx-sitemap warning: No pages generated for %s" %
              app.config.sitemap_filename)
        return

    ET.register_namespace('xhtml', "http://www.w3.org/1999/xhtml")

    root = ET.Element("urlset")

    if not urlset:
        root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
    else:
        for item in urlset:
            root.set(*item)

<<<<<<< HEAD
    locales = get_locales(app, exception)
=======
    locales = get_locales(app)
>>>>>>> ba86d7460e (new bulild changes)

    if app.builder.config.version:
        version = app.builder.config.version + '/'
    else:
        version = ""
    
    while True:
        try:
            link = app.env.app.sitemap_links.get_nowait()
            print(link)  # type: ignore
        except queue.Empty:
            break

        url = ET.SubElement(root, "url")
        scheme = app.config.sitemap_url_scheme
        if app.builder.config.language:
            lang = app.builder.config.language + '/'
        else:
            lang = ""

        ET.SubElement(url, "loc").text = site_url + scheme.format(
            lang=lang, version=version, link=link
        )

        if meta:
            for entry in meta:
                namespace, values = entry
                namespace_element = ET.SubElement(url, namespace)
                for tag_name, tag_value in values.items():
                    ET.SubElement(namespace_element, tag_name).text = tag_value

<<<<<<< HEAD
        if len(app.locales) > 0:
=======
        if len(locales) > 0:
>>>>>>> ba86d7460e (new bulild changes)
            for lang in locales:
                lang = lang + '/'
                linktag = ET.SubElement(
                    url,
                    "{http://www.w3.org/1999/xhtml}link"
                )
                linktag.set("rel", "alternate")
                linktag.set("hreflang",  hreflang_formatter(lang.rstrip('/')))
                linktag.set("href", site_url + scheme.format(
                    lang=lang, version=version, link=link
                ))

    filename = Path(app.outdir) / app.config.sitemap_filename
    ET.ElementTree(root).write(filename,
                               xml_declaration=True,
                               encoding='utf-8',
                               method="xml")
    print("%s was generated for URL %s in %s" % (app.config.sitemap_filename,
          site_url, filename))
