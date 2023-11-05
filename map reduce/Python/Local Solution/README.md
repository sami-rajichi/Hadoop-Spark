# MapReduce Total Sales Per Store

## Introduction

A MapReduce job consists primarily of two types of programs:

- **Mappers**: These programs extract the necessary data in key/value format to enable sorting by key.
- **Reducers**: They take a set of data sorted by their key and perform the necessary processing on this data (sum, average, total, etc.).

## Task: Total Sales per Store

Imagine you have multiple stores that you manage around the world. The goal is to calculate the total sales per store for a file with fields in the following format:

**Date Time Store Product Cost Payment**

## Getting Started (Run Locally)

To calculate sales per store, we extract key-value pairs in the form (store, cost). The Mapper extracts these pairs, and the Reducer's job is to sum the costs for the same store.

In this Jupyter Notebook, we'll test a MapReduce program, Purchases (TotalSalesPerStore), for sales data processing. TotalSalesPerStore calculates total revenue per store, breaking the calculation into two steps:

- **Mapping step**: We extract information about each store and its associated cost, delivering a textual stream as output. Each line contains the store identifier and its cost.

- **Reducing step**: We sum the costs for each store to find the total revenue for each store in the data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
