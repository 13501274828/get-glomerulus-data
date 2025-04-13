# get-glomerulus-data

本项目用于从 PubMed 和 PubMed Central 中自动获取肾小球的标注数据，包括图像（images）和图说（captions）。

> This project is used to automatically obtain labeled data of glomeruli, including images and captions, from PubMed and PubMed Central.

---

## 📁 Project Structure

```bash
.
├── pubmed.ipynb               # 获取 PubMed 中的图文数据 / Obtain data from PubMed
├── pubmed_central.ipynb       # 获取 PubMed Central 中的图文数据 / Obtain data from PubMed Central
├── paper_list.ipynb           # 对数据进行筛选和分类 / Classify and filter the data list
├── requirements.txt           # 项目依赖包列表 / Dependency list
├── .gitignore                 # 忽略规则文件 / Git ignore rules
└── README.md                  # 项目说明文件 / This documentation
```

### For Step 1 in `pubmed.ipynb` and `pubmed_central.ipynb`, if you want to change the search keywords, you can modify the following line:

```python
url = f'https://openi.nlm.nih.gov/gridquery?q=glomerulus&m={m}&n={n}&it=xg'
```

For example：
To use multiple keywords, replace the value after q=. For example, to search for "glomerulus glomeruli glomerular", update the line to: url = f'https://openi.nlm.nih.gov/gridquery?q=glomerulus%20glomeruli%20glomerular&m={m}&n={n}&it=xg'

Note: Use %20 to separate multiple keywords in the query string. Each additional keyword must be separated by one %20.

MIT License

Copyright (c) 2025 [Daniel Guo]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in  
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN  
THE SOFTWARE.
