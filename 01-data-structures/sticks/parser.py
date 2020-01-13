import os
from collections import Counter
from decimal import Decimal


def parse_value(value):
    if value == "null":
        return None
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value


def parse(data):

    data = data.strip().lstrip("{").rstrip("}").strip()
    data = set(data.split("}, {"))

    result = []

    for dict_data in data:
        dict_data = dict_data.strip().lstrip("\"")
        dict_data = dict_data.split(', \"')
        _item = {}
        for elem_str in dict_data:
            key, value = tuple(elem_str.split("\": "))
            key, value = key.rstrip("\""), value.lstrip("\"").rstrip("\"")
            _item.update({key: parse_value(value)})
        result.append(_item)
    return result


def dump_object(obj):

    inner = ", ".join(
        [f"{dump_string(key)}: {dump_map[type(value)](value)}"
         for key, value in obj.items()]
    )
    return "".join(["{", inner, "}"])


def dump_array(obj):
    inner = ", ".join(list(
        map(lambda x: dump_map[type(x)](x), obj)
    ))
    return f"[{inner}]"


def dump_int(obj):
    return f"{obj}"


def dump_float(obj):
    return f"\"{obj}\""


def dump_none(_):
    return "null"


def dump_string(obj):
    return f"\"{obj}\""


def dump_boolean(obj):
    if obj:
        return "true"
    return "false"


dump_map = {
    dict: dump_object,
    list: dump_array,
    tuple: dump_array,
    set: dump_array,
    int: dump_int,
    float: dump_float,
    type(None): dump_none,
    str: dump_string,
    bool: dump_boolean
}


def dump_json(obj):
    return dump_map[type(obj)](obj)


def create_markdown(data):

    def value_to_string(value):
        if isinstance(value, list):
            return ", ".join(value)
        return str(value)

    wines_titles = {
        "average_price": "Average price",
        "min_price": "Min. price",
        "max_price": "Max. price",
        "most_common_region": "Most common region",
        "most_common_country": "Most common country",
        "average_score": "Average score"
    }

    common_titles = {
        "most_expensive_wine": "Most expensive wine",
        "cheapest_wine": "Cheapest wine",
        "highest_score": "Highest score",
        "lowest_score": "Lowest score",
        "most_expensive_country": "Most expensive country",
        "cheapest_country": "Cheapest country",
        "most_rated_country": "Most rated country",
        "underrated_country": "Underrated country",
        "most_active_commentator": "Most active commentator"
    }

    result = "# Statistics\n"
    result += "### Wines\n"
    result += "| Variety | " + " | ".join(wines_titles.values()) + " |\n"
    result += " | ".join(["---"] * (len(wines_titles) + 1)) + " |\n"
    for wine, wine_data in data["statistics"]["wine"].items():
        result += f"| {wine} | "
        result += " | ".join([
            value_to_string(wine_data[key]) for key in wines_titles.keys()
        ]) + " |\n"

    result += "\n" * 3

    for key, title in common_titles.items():
        result += f"#### {title}"
        value = data["statistics"][key]
        if isinstance(value, list):
            result += ":\n"
            result += "\n".join([f"* {v}" for v in value])
            result += "\n"
        else:
            result += f": {value} \n"

    result += "\n" * 3
    return result


def get_statistics(wines):
    # total
    t_stat = {
        'most_expensive_wine': [],
        'cheapest_wine': [],
        'price_min': None,
        'price_max': 0,
        'highest_score': [],
        'lowest_score': [],
        'score_min': None,
        'score_max': 0,
        'commentators': Counter(),
        'price_country_cnt': Counter(),
        'price_country_sum': Counter(),
        'price_country_avg': Counter(),
        'score_country_cnt': Counter(),
        'score_country_sum': Counter(),
        'score_country_avg': Counter(),
    }
    variety_stat = {}

    for wine in wines:
        country = wine['country']
        description = wine['description']
        designation = wine['designation']
        points = wine['points']
        price = wine['price']
        province = wine['province']
        region_1 = wine['region_1']
        region_2 = wine['region_2']
        taster_name = wine['taster_name']
        taster_twitter_handle = wine['taster_twitter_handle']
        title = wine['title']
        variety = wine['variety']
        winery = wine['winery']

        if taster_name is not None:
            t_stat['commentators'][taster_name] += 1

        v_stat = variety_stat.setdefault(variety, {
            'price_count': 0,
            'price_sum': 0,
            'price_avg': 0.0,
            'price_min': None,
            'price_max': 0,
            'score_count': 0,
            'score_sum': 0,
            'score_avg': 0.0,
            'region': Counter(),
            'country': Counter(),
        })

        if price:
            v_stat['price_count'] += 1
            v_stat['price_sum'] += price
            v_stat['price_avg'] = v_stat['price_sum'] / v_stat['price_count']

            variety_min_price = v_stat['price_min']
            if variety_min_price is None or variety_min_price > price:
                v_stat['price_min'] = price

            variety_max_price = v_stat['price_max']
            if variety_max_price < price:
                v_stat['price_max'] = price

            t_min_price = t_stat['price_min']
            if t_min_price is None or t_min_price > price:
                t_stat['price_min'] = price
                t_stat['cheapest_wine'] = [title]
            elif t_min_price == price:
                t_stat['cheapest_wine'].append(title)

            t_max_price = t_stat['price_max']
            if t_max_price < price:
                t_stat['price_max'] = price
                t_stat['most_expensive_wine'] = [title]
            elif t_max_price == price:
                t_stat['most_expensive_wine'].append(title)

            t_stat['price_country_cnt'][country] += 1
            t_stat['price_country_sum'][country] += price

            p_sum = t_stat['price_country_sum'][country]
            p_count = t_stat['price_country_cnt'][country]
            t_stat['price_country_avg'][country] = p_sum / p_count

        if region_1:
            v_stat['region'][region_1] += 1
        if region_2:
            v_stat['region'][region_2] += 1

        v_stat['country'][country] += 1

        if points:
            v_stat['score_count'] += 1
            v_stat['score_sum'] += points
            v_stat['score_avg'] = v_stat['score_sum'] / v_stat['score_count']

            t_min_score = t_stat['score_min']
            if t_min_score is None or t_min_score > points:
                t_stat['score_min'] = points
                t_stat['lowest_score'] = [title]
            elif t_min_score == points:
                t_stat['lowest_score'].append(title)

            t_max_score = t_stat['score_max']
            if t_max_score < points:
                t_stat['score_max'] = points
                t_stat['highest_score'] = [title]
            elif t_max_score == points:
                t_stat['highest_score'].append(title)

            t_stat['score_country_cnt'][country] += 1
            t_stat['score_country_sum'][country] += points

            s_sum = t_stat['score_country_sum'][country]
            s_count = t_stat['score_country_cnt'][country]
            t_stat['score_country_avg'][country] = s_sum / s_count

    return t_stat, variety_stat


def get_most_common(counter, is_min=False):
    most_common = counter.most_common()
    if not most_common:
        return []
    if is_min:
        value = most_common[-1][1]
    else:
        value = most_common[0][1]

    return list((item for item, count in most_common if count == value))


if __name__ == "__main__":

    base_path = os.path.abspath(os.path.dirname(__file__))

    with open(os.path.join(base_path, "winedata_1.json"), "r") as wine_file_1:
        wine_data_1 = "".join(wine_file_1.readlines())\
            .strip().lstrip("[").rstrip("]").strip()

    with open(os.path.join(base_path, "winedata_2.json"), "r") as wine_file_2:
        wine_data_2 = "".join(wine_file_2.readlines())\
            .strip().lstrip("[").rstrip("]").strip()

    wines_data = parse(", ".join([wine_data_1, wine_data_2]))
    total_statistics, variety_statistics = get_statistics(wines_data)

    selected_varieties = [
        "Gew\\u00fcrztraminer", "Riesling", "Merlot",
        "Madera", "Tempranillo", "Red Blend"
    ]

    statistics_wine = {
        variety: {
            "average_price": str(
                Decimal(variety_stat['price_avg']).quantize(Decimal("0.01"))
            ),
            "min_price": variety_stat['price_min'],
            "max_price": variety_stat['price_max'],
            "most_common_region": get_most_common(variety_stat['region']),
            "most_common_country": get_most_common(variety_stat['country']),
            "average_score": str(
                Decimal(variety_stat['score_avg']).quantize(Decimal("0.01"))
            )
        } for variety, variety_stat in variety_statistics.items()
        if variety in selected_varieties
    }

    statistics = {
        "statistics": {
            "wine": statistics_wine,
            "most_expensive_wine": total_statistics['most_expensive_wine'],
            "cheapest_wine": total_statistics['cheapest_wine'],
            "highest_score": total_statistics['score_max'],
            "lowest_score": total_statistics['score_min'],
            "most_expensive_country": get_most_common(
                total_statistics['price_country_avg']
            ),
            "cheapest_country": get_most_common(
                total_statistics['price_country_avg'],
                is_min=True
            ),
            "most_rated_country": get_most_common(
                total_statistics['score_country_avg']
            ),
            "underrated_country": get_most_common(
                total_statistics['score_country_avg'],
                is_min=True
            ),
            "most_active_commentator": get_most_common(
                total_statistics['commentators']
            )
        }
    }

    with open(os.path.join(base_path, "stats.json"), "w") as output_json:
        output_json.write(dump_json(statistics))

    with open(os.path.join(base_path, "stats.md"), "w") as output_json:
        output_json.write(create_markdown(statistics))