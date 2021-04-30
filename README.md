# Major Project - Covid19 Forcast and effect of lockdown/vaccination (BITS F464)

This project is done as a part of the major project under the course BITS F464 course.

Contributors :-

1. Sanchit Krishna	(2017AAPS0223G)
2. Mudit Agarwal 	(2017B3A70483G)
3. Shashwat Oorjit Avasthi	(2017A3PS0459G)
4. Mayank Chaturvedi	(2017B4A70548G)
5. Chetan Khanna	(2017B4A70591G)

The directory structure for the repo is as follows:-

```bash
./
├── data
│   ├── cases_data
│   │   ├── active_cases_data.csv
│   │   ├── cases.csv
│   │   └── source.txt
│   ├── data.csv
│   ├── data.ods
│   ├── deaths_data
│   │   ├── deaths_modified.csv
│   │   ├── deaths_org.csv
│   │   └── deaths_scrape.py
│   ├── mobility_data
│   │   ├── apple_mobility.csv
│   │   ├── applemobilitytrends-2021-04-20.csv
│   │   └── Copy of mobilityUK.ipynb
│   └── vaccine_data
│       ├── org.csv
│       ├── vaccine_dose1.csv
│       ├── vaccine_dose2.csv
│       └── vaccine_scrape.py
├── README.md
└── src
    ├── Experiment.ipynb
    └── FinalSubmit.ipynb
```

The `data` directory contains all the scraped and downloaded data while the `src` directory has the notebooks we used for making the report. The `data` directory also contains code snippets used for scraping data from the net and/or links from where the data was downloaded.

The code snippets in the `data` directory also apply **data preprocessing** steps since it was more convinient to apply them at the source due to the limited data that we use.

There are following subdirectories in this folder which contain the following data:-

1. cases_data: This folder has all the data related to active, cummulative and newly reported cases on a daily basis in London

2. deaths_data: This folder has all the data related to daily and cummulative deaths that occured in London

3. mobility_data: The mobility data from Apple is used to determine the level of activity in the streets of London and hence gauge the level of lockdown that was observed during the period.

4. vaccine_data: This contains vaccine related data -- both first and second shot.

Once all the data was scrapped, we combined it manually in Excel. This was way easier than doing it progamatically since the data was limited.
The combined data is present in `data.csv` file (obtained from `data.ods`).

The `src` folder had two jupyter notebooks -- Experiment and FinalSubmit. The former one was used to access and try different models. FinalSubmit contains the code and results that we have used for our report. It is a formatted and easier to read version of the Experiment notebook.

**NOTE**: The link for wandb report is here: https://wandb.ai/pct101/final_submission/
**NOTE**: The link for the colab notebook is here: https://colab.research.google.com/drive/1HFNcCuNCEIZUmiPAf1krxoQu_NC9qI6p?usp=sharing
