# quarto-viz-demo

A small [Quarto](https://quarto.org) document showing several ways to build interactive charts:

1. **Altair**: a brushable scatter plot linked to a bar chart
2. **Vega-Lite**: a raw spec rendered through Altair
3. **Observable Plot**: in an `{ojs}` cell
4. **D3**: Python data passed to Observable JS with `ojs_define`

Live page: https://colemanto.github.io/quarto-viz-demo/

There's also a [Quarto dashboard](dashboard.qmd) of the penguins data (value boxes and three Observable Plot charts, with sidebar filters), published at `/dashboard.html`.

## Run locally

Requires [Quarto](https://quarto.org/docs/get-started/) and Python 3.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
QUARTO_PYTHON=.venv/bin/python quarto preview index.qmd
```

## Publishing

Pushes to `main` trigger [.github/workflows/publish.yml](.github/workflows/publish.yml), which renders the document and deploys it to GitHub Pages. In the repo settings, Pages must use **GitHub Actions** as its source.

## Notes

- Interactive charts need HTML output. For PDF or Word, Altair needs `vl-convert-python` (included in `requirements.txt`) to render static images.
- `penguins.csv` comes from [seaborn-data](https://github.com/mwaskom/seaborn-data).
