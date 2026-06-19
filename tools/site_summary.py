import json
from typing import List, Dict, Any


SITE_DATA: Dict[str, Any] = {
    "site_name": "乐鱼体育门户",
    "homepage_url": "https://appm-leyu.com.cn",
    "keywords": ["乐鱼体育", "体育赛事", "在线娱乐", "竞技平台"],
    "tags": ["体育", "电竞赛事", "直播", "比分"],
    "description": "乐鱼体育是国内领先的综合性体育娱乐平台，提供赛事直播、数据分析和互动社区服务。",
    "popular_sections": [
        {"title": "篮球赛事", "url": "https://appm-leyu.com.cn/basketball", "hot": True},
        {"title": "足球联赛", "url": "https://appm-leyu.com.cn/football", "hot": True},
        {"title": "网球动态", "url": "https://appm-leyu.com.cn/tennis", "hot": False},
    ],
}


def format_keyword_list(keywords: List[str]) -> str:
    return "、".join(keywords)


def format_tag_list(tags: List[str]) -> str:
    return " | ".join(tags)


def build_summary_block(
    name: str,
    url: str,
    keywords: List[str],
    tags: List[str],
    description: str,
    sections: List[Dict[str, Any]],
) -> str:
    lines = []
    lines.append("=" * 50)
    lines.append(f"站点名称：{name}")
    lines.append(f"首页地址：{url}")
    lines.append(f"核心关键词：{format_keyword_list(keywords)}")
    lines.append(f"标签分类：{format_tag_list(tags)}")
    lines.append(f"简短说明：{description}")
    lines.append("")
    lines.append("热门栏目：")
    for sec in sections:
        hot_mark = " [热门]" if sec.get("hot") else ""
        lines.append(f"  - {sec['title']}{hot_mark} -> {sec['url']}")
    lines.append("=" * 50)
    return "\n".join(lines)


def generate_summary_to_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "site_name": data.get("site_name"),
        "homepage_url": data.get("homepage_url"),
        "keywords": data.get("keywords"),
        "tags": data.get("tags"),
        "description": data.get("description"),
        "section_count": len(data.get("popular_sections", [])),
    }


def display_summary(data: Dict[str, Any]) -> None:
    summary_text = build_summary_block(
        name=data["site_name"],
        url=data["homepage_url"],
        keywords=data["keywords"],
        tags=data["tags"],
        description=data["description"],
        sections=data["popular_sections"],
    )
    print(summary_text)


def export_summary_json(data: Dict[str, Any], output_path: str = "site_summary.json") -> None:
    summary_dict = generate_summary_to_dict(data)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(summary_dict, f, ensure_ascii=False, indent=2)
    print(f"摘要 JSON 已保存至：{output_path}")


def main() -> None:
    display_summary(SITE_DATA)
    export_summary_json(SITE_DATA)


if __name__ == "__main__":
    main()