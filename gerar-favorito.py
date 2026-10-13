"""Gera favorito.txt (o endereço "javascript:..." do favorito) a partir de conferir-gestao.js.

Uso:
  python3 -I gerar-favorito.py
"""
from pathlib import Path
from urllib.parse import quote

RAIZ = Path(__file__).resolve().parent


def main():
    js = (RAIZ / "conferir-gestao.js").read_text(encoding="utf-8")
    url = "javascript:" + quote(js, safe="()*'!~")
    (RAIZ / "favorito.txt").write_text(url, encoding="utf-8")
    print(f"favorito gerado ({len(url)} caracteres)")


if __name__ == "__main__":
    main()
