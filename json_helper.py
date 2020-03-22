{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import os\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def read_json(path):\n",
    "    with open(path, 'r') as f:\n",
    "        data = json.load(f)\n",
    "        return data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def json_df_generator(JSON_ROOT):\n",
    "    for direpath, direnames, filenames in os.walk(JSON_ROOT):\n",
    "        results = []\n",
    "        for f in filenames:\n",
    "            if f.endswith('.json'):\n",
    "                json_content = read_json(os.path.join(JSON_ROOT,f))\n",
    "                for i in json_content['results']:\n",
    "                    results.append(i)\n",
    "    df = pd.DataFrame(results)\n",
    "    return df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
