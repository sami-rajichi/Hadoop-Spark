# Hadoop MapReduce Solutions

## Introduction

In this project, we explore two solutions for performing MapReduce tasks using Hadoop. A MapReduce job typically involves two types of programs:

- **Mappers**: These programs extract data in key/value format for sorting by key.
- **Reducers**: They process sorted data, performing tasks such as summing, averaging, and more.

## Task: Total Sales per Store

Imagine you have multiple stores that you manage around the world. The goal is to calculate the total sales per store for a file with fields in the following format:

**Date Time Store Product Cost Payment**

## Solution 1: Using mrjob

### Introduction

Solution 1 uses the `mrjob` library, which simplifies the process of writing Python programs that run on Hadoop. This solution allows you to test your code locally without installing Hadoop and run it on a cluster of your choice.

## Solution 2: Classic MapReduce

### Introduction

Solution 2 is the classic approach for performing MapReduce tasks with Hadoop. It provides a traditional method for data processing on Hadoop clusters.

### Features

- **Python Version**: Ensure that each Hadoop container has the same Python version exported as the default environment variable.

- **Script Headers**: Each script (Map and Reduce script) should begin with `#!/usr/bin/env python` to ensure consistency and compatibility across the cluster.

## Getting Started

To run these MapReduce solutions with Hadoop, follow these general steps:

1. Set up a Hadoop cluster or a local Hadoop environment.

2. Ensure that Python is installed on all containers and that the same version is set as the default environment variable.

3. Ensure that each script (Map and Reduce script) begins with `#!/usr/bin/env python` for consistency.

By following these guidelines, you can run your MapReduce jobs smoothly and consistently across your Hadoop cluster. Failure to comply with these recommendations may lead to errors and inconsistencies in your data processing.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
