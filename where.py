import pandas as pd

df = pd.read_csv("city/output/list_of_countries.csv")

def run_country_checker():
    while True:
        try:
            your_country = input("What is your country? ")
            float(df[df.country == your_country]["purchasing_power_index"])
        except TypeError:
            print(f"'{your_country}' is an invalid country. Please try again.")
        else:
            your_country = your_country.lower()
            your_country = your_country.title()
            return your_country

your_country = run_country_checker()

def _value_checker(index_input):
    if index_input == '':   # empty string, default index
        return "default"
    else:
        try:
            return float(index_input)
        except ValueError:
            return False


def purchase_power():
    your_purchasing_power_index = float(
        df[df.country == your_country]["purchasing_power_index"]
    )
    print(f"In your country purchasing power index is {your_purchasing_power_index}")

    while True:
        index_input = (
            input("What is your desirable purchasing power index (higher is better)? ")
        )
        if type(_value_checker(index_input)) == float:
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return your_purchasing_power_index
        else:
            print(f"'{index_input}' is an invalid index. Please try again.")


def safety_index():
    your_safety_index = float(
        df[df.country == your_country]["safety_index"]
    )
    print(f"In your country safety index is {your_safety_index}")

    while True:
        index_input = (
            input("What is your desirable safety index (higher is better)? ")
        )
        if type(_value_checker(index_input)) == float:
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return your_safety_index
        else:
            print(f"'{index_input}' is an invalid index. Please try again.")


def health_care_index():
    your_health_care_index = float(
        df[df.country == your_country]["health_care_index"]
    )
    print(f"In your country health care index is {your_health_care_index}")

    while True:
        index_input = (
            input("What is your desirable health care index (higher is better)? ")
        )
        if type(_value_checker(index_input)) == float:
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return your_health_care_index
        else:
            print(f"'{index_input}' is an invalid index. Please try again.")


def climate_index():
    your_climate_index = float(
        df[df.country == your_country]["climate_index"]
    )
    print(f"In your country climate index is {your_climate_index}")

    while True:
        index_input = (
            input("What is your desirable climate index (higher is better)? ")
        )
        if type(_value_checker(index_input)) == float:
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return your_climate_index
        else:
            print(f"'{index_input}' is an invalid index. Please try again.")


def cost_of_living_index():
    your_cost_of_living_index = float(
        df[df.country == your_country]["cost_of_living_index"]
    )
    print(f"In your country cost of living index is {your_cost_of_living_index}")

    while True:
        index_input = (
            input("What is your desirable cost of living index (lower is better)? ")
        )
        if type(_value_checker(index_input)) == float:
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return your_cost_of_living_index
        else:
            print(f"'{index_input}' is an invalid index. Please try again.")


def property_price_to_income_ratio():
    your_property_price_to_income_ratio = float(
        df[df.country == your_country]["property_price_to_income_ratio"]
    )
    print(f"In your country house price to income ratio index is {your_property_price_to_income_ratio}")

    while True:
        index_input = (
            input("What is your desirable house price to income ratio (lower is better)? ")
        )
        if type(_value_checker(index_input)) == float:
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return your_property_price_to_income_ratio
        else:
            print(f"'{index_input}' is an invalid index. Please try again.")


def traffic_commute_time_index():
    your_traffic_commute_time_index = float(
        df[df.country == your_country]["traffic_commute_time_index"]
    )
    print(f"In your country traffic commute time index is {your_traffic_commute_time_index}")

    while True:
        index_input = (
            input("What is your desirable traffic commute time index (lower is better)? ")
        )
        if type(_value_checker(index_input)) == float:
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return your_traffic_commute_time_index
        else:
            print(f"'{index_input}' is an invalid index. Please try again.")


def pollution_index():
    your_pollution_index = float(
        df[df.country == your_country]["pollution_index"]
    )
    print(f"In your country pollution index is {your_pollution_index}")

    while True:
        index_input = (
            input("What is your desirable pollution index (lower is better)? ")
        )
        if type(_value_checker(index_input)) == float:
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return your_pollution_index
        else:
            print(f"'{index_input}' is an invalid index. Please try again.")

            
values = {
    "purchasing_power_index": 200,
    "safety_index": 200,
    "health_care_index": 200,
    "cost_of_living_index": 0,
    "property_price_to_income_ratio": 0,
    "traffic_commute_time_index": 0,
    "pollution_index": 0,
    "climate_index": 200,
}
df = df.fillna(value=values)

#where functions run
your_purchasing_power_index = float(purchase_power())
your_safety_index = float(safety_index())
your_health_care_index = float(health_care_index())
your_climate_index = float(climate_index())
your_cost_of_living_index = float(cost_of_living_index())
your_property_price_to_income_ratio = float(property_price_to_income_ratio())
your_traffic_commute_time_index = float(traffic_commute_time_index())
your_pollution_index = float(pollution_index())


out_df = df[(df.purchasing_power_index > your_purchasing_power_index) &
            (df.safety_index > your_safety_index) &
            (df.health_care_index > your_health_care_index) &
            (df.cost_of_living_index < your_cost_of_living_index) &
            (df.property_price_to_income_ratio <
                your_property_price_to_income_ratio) &
            (df.traffic_commute_time_index <
                your_traffic_commute_time_index) &
            (df.pollution_index < your_pollution_index) &
            (df.climate_index > your_climate_index)]

print_out_df = out_df[
    ["country", "freedomhouse_score", "quality_of_life_index"]
].dropna().sort_values(by=['freedomhouse_score'], ascending=False)

if print_out_df.empty:
    print(f"There is no country better than {your_country}.")
else:
    with pd.option_context("display.max_rows", None, "display.max_columns", None):
        print(print_out_df)
