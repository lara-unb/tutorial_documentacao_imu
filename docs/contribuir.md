# Como contribuir

## Novo guia

1. Crie uma pasta em `tutoriais/` com o nome do guia, como `tutoriais/leitura_uma_imu/`.
2. Escreva o guia em um arquivo `.md` dentro dela e coloque as imagens em `imagens/`.
3. Inclua o guia no nível correspondente: no `nav` do `mkdocs.yml` e na tabela da página do nível.

Os guias continuam legíveis direto no GitHub; o site apenas os reúne. O formato segue o da [Primeira coleta](tutoriais/primeira_coleta/primeira_coleta_tutorial.md): passos numerados e marcações (1), (2)… nas imagens.

## Visualização local

```bash
pip install mkdocs-material==9.7.7
mkdocs serve
```

O site abre em `http://127.0.0.1:8000`.

## Publicação

A cada push na `main`, o GitHub Actions gera o site e publica na branch `gh-pages`.
