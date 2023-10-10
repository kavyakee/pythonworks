from json import load
path="C:\\Users\\Admin\\Desktop\\luminar_python\\countries\\countries.json"
with open(path,encoding="utf-8") as f:
    countries=load(f)
print(len(countries))

# to read a jason file => load
# to convert a string  => loads


# to print the country names
country_name=[c.get("name") for c in countries]
print(country_name)
# to print the capital of a country
country_capital=[c.get("capital") for c in countries if c.get("name")=="Saudi Arabia"]
print(country_capital)

# to print all regions
region_all={c.get("region") for c in countries }     # here {} is used to prevent the duplicates from printing.
print(region_all)


# to print the borders of india
country_border=[c.get("borders") for c in countries if c.get("name")=="India"][0]                     #[0] is used to remove the [] from the terminal.
print(country_border)
border_name=[c.get("name") for c in countries if c.get("alpha3code") in country_border]
print(border_name)

# print independ3nt country names
# print currency name of India
# india_currency=[c.get("currencies")for c in countries if c.get("name"=="India")]
# print(india_currency.get("name"))

data=[c.get("name") for c in countries if "currencies" not in c]
print(data)

# to print the coutries using currencies
country_currency=[c for c in countries if "currencies" in c]
currencies=[c.get("currencies")[0].get("symbol") for c in country_currency]
wc={}
for c in currencies:
    if c in wc:
        wc[c]+=1
    else:
        wc[c]=1
print(max((v,k)for k,v in wc.items()))