# A Novel Reselection Approach to Address Matthew Effect in Recommender Systems
<h4>Jenny Sheng</h4>
<h4>Princeton University Class of 2022</h4>
<h4>Advised by Dr. Xiaoyan Li</h4>

## Background
This repository contains the code written for the paper "A Novel Reselection Approach to Address Matthew Effect in Recommender Systems" completed in fall 2020 under the advisement of Dr. Xiaoyan Li. The goal of this project is to discover a novel, alternative way of addressing Matthew Effect in recommender systems that actively includes long-tail items as part of the recommendation list while avoiding any substantial reworkings of existing recommender systems. In this sense, the project strives to break this vicious cycle through actively replacing some portion of the recommendations with items that are less popular, thereby exposing the user to some long-tail items and allowing these items to gain exposure and ratings. It is very different from existing post-processing approaches because the current approaches are largely centered around reweighing predicted ratings to account for diversity or novelty, whereas this paper presents a post-processing algorithm that is based on generating a probability distribution using random walk with restart.

## Data Set
The data set that we chose to use and test with is the Movielens 20M data set. We only included movies with greater than or equal to 20 ratings in total, and only include users with greater than or equal to 20 ratings. This cutoff ensures that every movie included in the data set is either in the short-head or the long-tail. After performing the cutoff, we took a random sample of 10% of users to use as part of the data set because of computation limits.

## Usage
There are three main files, each is available in python code and as Jupyter Notebooks. baseline_results.ipynb generates results from baseline algorithms such as SVD and NMF. The results from baseline_results.ipynb is then fed into personalized_reranking.ipynb, where we generate results using personalized reranking as a point of comparison. The results from personalized_reranking.ipynb is then fed into rwr_reselection.ipynb to generate results using our RWR post-processing reselection algorithm. rwr_reselection.ipynb also contains the code to calculate the following metrics: MAP@K, prediction coverage, average coverage of long-tail items, novelty, personalization, and intra-list similarity.
