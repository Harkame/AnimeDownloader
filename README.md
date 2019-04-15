# AnimeDownloader

## Mentions

https://github.com/gius-italy/openload-dl

## Installation

``` bash
pip install -r requirements.txt
```

### Run

``` bash
python animedownloader/main.py
```

### Options

``` bash

```

### How it work

This program use an config file (default : ./config.yml)

This file contains list of animes to download, destination path, etc.

#### Example  of config file

``` yaml
animes:
  - anime:
      https://www.jetanime.co/anime/shingeki-no-kyojin-saison-3/
  - episode:
      https://www.jetanime.co/shingeki-no-kyojin-saison-3-episode-9-vostfr/

destination_path:
  ./animes/
```

## Test

``` bash
  pip install tox

  tox
```
