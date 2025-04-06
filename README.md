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
