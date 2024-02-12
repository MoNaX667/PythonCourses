from argparse import ArgumentParser
from typing import List, Optional, Sequence
import requests
import xml.etree.ElementTree as ET
import json


class UnhandledException(Exception):
    pass


def rss_parser(xml: str, limit: Optional[int] = None, as_json: bool = False) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        as_json: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as separate lines.
    """
    # Parse XML
    root = ET.fromstring(xml)

    # Extract channel information
    channel_info = {}
    items = []

    for child in root.find('channel'):
        tag_name = child.tag
        tag_text = child.text.strip() if child.text else ""

        if tag_name == "category":
            if "categories" not in channel_info:
                channel_info["categories"] = []
            channel_info["categories"].append(tag_text)
        else:
            channel_info[tag_name] = tag_text

    # Extract items information
    for item in root.findall('.//item'):
        item_info = {}

        for child in item:
            tag_name = child.tag
            tag_text = child.text.strip() if child.text else ""

            item_info[tag_name] = tag_text

        items.append(item_info)

    # Format output
    output = []
    if not as_json:
        # Channel information
        output.append(f"Feed: {channel_info.get('title', '')}")
        output.append(f"Link: {channel_info.get('link', '')}")
        output.append(f"Last Build Date: {channel_info.get('lastBuildDate', '')}")
        output.append(f"Publish Date: {channel_info.get('pubDate', '')}")
        output.append(f"Language: {channel_info.get('language', '')}")
        output.append("Categories: " + ', '.join(channel_info.get('categories', [])))
        output.append(f"Managing Editor: {channel_info.get('managingEditor', '')}")
        output.append(f"Description: {channel_info.get('description', '')}")

        # Items information
        for item in items[:limit]:
            output.append("")
            output.append(f"Title: {item.get('title', '')}")
            output.append(f"Author: {item.get('author', '')}")
            output.append(f"Published: {item.get('pubDate', '')}")
            output.append(f"Link: {item.get('link', '')}")
            output.append(f"Categories: {item.get('category', '')}")
            output.append(f"Description: {item.get('description', '')}")
    else:
        # JSON output
        json_output = {
            "title": channel_info.get('title', ''),
            "link": channel_info.get('link', ''),
            "description": channel_info.get('description', ''),
            "items": items[:limit] if limit else items
        }
        output.append(json.dumps(json_output, indent=2))

    return output


def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", dest="as_json", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)
    xml = requests.get(args.source).text
    try:
        print("\n".join(rss_parser(xml, args.limit, args.as_json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()