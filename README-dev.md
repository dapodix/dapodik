# Panduan Pengembang

> Panduan belum selesai

## Install

1. [Install python-poetry](https://python-poetry.org/docs/#osx-linux-bashonwindows-install-instructions)
2. Clone project

    ```bash
    git clone https://github.com/dapodix/dapodik.git
    ```

3. Install dependencies

    ```bash
    poetry install --no-root
    ```

4. Selesai.

## Guideline

### Import

1. Diusahakan immport berurutan, dan `import \*` diatas `from \* import \*`

   ```python
   import abc
   import xyz
   from abc import de
   from efg import hi
   ```

2. Import internal harus dibawah import external dengan jarak 1 newline kosong.

### Kontainer dataclass

#### Update

Jika data dapat diupdate maka pastikan sesuai dengan aturan berikut

```python
from typing import Optional

from dapodik.base import dataclass, freeze


@dataclass
class Foo:
    bar: str = freeze(default=None) # Tidak akan dimasukan put request
    ban: str = None # Tidak akan dimasukan put request
    baz: Optional[str] = None # Akan dimmasukan ke dalam put request, meskipun null
```

#### Frozen

Data yang tidak dapat dirubah / hanya dapat diambil harus dibuat *frozen*, dan jika memungkinkan juga dibuat *slots*.

```python
from dapodik.base import dataclass


@dataclass(frozen=True, slots=True)
class DataPermanen:
    a: str
    b: int
```
