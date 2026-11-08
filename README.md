# Holidays Calculator for Protugal

<div align="center">

![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=flat)
![Gitlab Pipeline Status](https://gitlab.com/majramos/holidays-pt/badges/main/pipeline.svg)
![Gitlab Release](https://gitlab.com/majramos/holidays-pt/-/badges/release.svg)
![Gitlab Coverage](https://gitlab.com/majramos/holidays-pt/badges/main/coverage.svg)

</div>

Package to dynamically calculate the holidays dates from Portugal, both national
and regional holidays for each district and county.


## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install holidays.

```bash
git clone https://gitlab.com/majramos/holidays-pt.git

cd holidays-pt

pip install holidays
```

or 
```bash
python -m pip install git+https://gitlab.com/majramos/holidays-pt.git
```


## Usage/Examples
```python
from holidays_pt import Holidays

hol = Holidays("2021-01-01", "2021-12-31")
hol.calculate().as_list()
[
    {
        "extent": "national",
        "label": "Ano Novo",
        "calculate": "january 1st",
        "date": datetime.datetime(2020, 1, 1, 0, 0),
    },
    ...,
]
```

A more complete example can be found in the [example notebook](/notebooks/example.ipynb)


## Software dependencies
- python>=3.13


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Check [CONTRIBUTING.md](./CONTRIBUTING.md).

Please make sure to update tests as appropriate.

## License
[GPLv3](https://choosealicense.com/licenses/gpl-3.0/)


# Notes

Can return holidays in various formats: list, table, timeseries.

Can calculate the count of business days for different fequencies.
