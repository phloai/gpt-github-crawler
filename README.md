# GPT GitHub Crawler
A tool that crawls GitHub repositories instead of sites. Enabling users to crawl repository trees, match file patterns, and decode file contents. This tool is ideal for extracting and processing data from repositories to upload to your custom GPT.

## Features
- **Recursive GitHub Repository Crawling:** Efficiently traverses the GitHub repository tree.
- **Pattern Matching:** Utilizes patterns to selectively crawl files in the repository.
- **Content Decoding:** Automatically decodes file contents for easy processing.
- **Configurable via JSON:** Allows easy configuration through an external `config.json` file by default, this can be altered with the `--config` flag.
- **JSON Output:** Outputs the crawled data into a structured JSON file.
- **Local Mode:** Supports crawling local repositories by specifying the local path in the configuration file and enabling local mode with the `--local` flag.

> [!NOTE]
> Remote repositories are crawled by default, unless local mode is enabled.

> [!TIP]
> For the fastest crawling it is recommended to clone the repository you want to crawl and run in local mode.

## Prerequisites
Before starting, ensure you have the following:
- Python 3.6 or higher.
- GitHub personal access token, if running on a remote repository.

## Installation
First, clone this repository:

```bash
git clone https://github.com/phloai/gpt-github-crawler.git
```

Then, navigate to the cloned directory:

```bash
cd gpt-github-crawler
```

### Setting Up the Environment
Install the required environment using Conda:

```bash
conda env create -f environment.yml
```

Activate the environment:

```bash
conda activate gpt-github-crawler
```

### Installing the Package
After activating the Conda environment, install the package in editable mode:

```bash
pip install -e .
```

This command installs the package and makes it available as a command-line tool. It also ensures that any changes you make to the code are immediately reflected when you run the tool.

## Configuration
The crawler script uses a configuration file named `config.json` by default, located in the same directory as the script. Create your configuration file with the following format:

```json
{
    "repo_owner": "<repository_owner>",
    "repo_name": "<repository_name>",
    "branch_name": "<branch_name>",
    "match": ["<pattern_to_match_files>", "**LICENSE",...],
    "ignore": ["<pattern_to_ignore_files>",...],
    "max_files_to_crawl": <max_number_of_files>,
    "output_file_name": "<output_filename>.json",
    "github_token": "<your_github_token>"
}
```

If running in `--local` mode, create your configuration with the following format:

```json
{
    "local_path": "<path_to_your_local_repo>",
    "match": ["<pattern_to_match_files>", "**LICENSE",...],
    "ignore": ["<pattern_to_ignore_files>",...],
    "max_files_to_crawl": <max_number_of_files>,
    "output_file_name": "<output_filename>.json"
}
```

> [!NOTE]
> It's recommended to keep `**LICENSE` in the match list, to always attach it to the output if it is available.
> 
> Ignore should be an empty list if you don't want to ignore any patterns.
> 
> The `output_file_name` accepts both absolute and relative paths. If a relative path is provided, it will be resolved relative to the directory where the **script is located.** It's recommended to always use absolute paths.

## Run your crawler
Once the package is installed and configuration file is created, you can run the script from anywhere in your system using the command:

```bash
gpt-github-crawler
```

This command will execute the crawler script according to the configuration specified in `config.json`. A JSON file will be generated with the results to the `output_file_name` path that is specified.

You can specify a different configuration file using the `--config` flag when running the script. For example, to use a configuration file located at `/path/to/your/config.json`, you can run the script like this:

```bash
gpt-github-crawler --config /path/to/your/config.json
```

> [!NOTE]
> This flag is optional, and accepts both absolute and relative paths. If a relative path is provided, it will be resolved relative to the directory where the **script is located.** It's recommended to always use absolute paths.

You can enable local mode by adding the `--local` flag when running the script. When enabled the script will iterate over all the files in the `local_path` specified in the configuration file. To enable local mode you should run the script like this:

```bash
gpt-github-crawler --local
```

> [!NOTE]
> The `local_path` should be a directory. It accepts both absolute and relative paths. If a relative path is provided, it will be resolved relative to the directory where the **script is being run on the command-line.** It's recommended to always use absolute paths.
> 
> When crawling `.ipynb` files, only source markdown and code cells will be included in the JSON file. Outputs will not be included.

## Contributing
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Create a new Pull Request.

> [!WARNING]
> Make sure to always check that your configuration and output files are **not** pushed. All JSON files in the root directory should be ignored by `.gitignore`, by default.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements
This project is inspired by and based on concepts from the [BuilderIO/gpt-crawler](https://github.com/BuilderIO/gpt-crawler).
