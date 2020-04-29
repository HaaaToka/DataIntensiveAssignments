

> Fix the name of the column showing the cuisine.

column_names = recipes.columns.values
column_names[0] = "cuisine"
recipes.columns = column_names

> Make all the cuisine names lowercase.

recipes["cuisine"] = recipes["cuisine"].str.lower()
recipes["cuisine"] = recipes["cuisine"].str.lower()

> Make the cuisine names consistent.

recipes.loc[recipes["cuisine"] == "austria", "cuisine"] = "austrian"
recipes.loc[recipes["cuisine"] == "belgium", "cuisine"] = "belgian"
...

> Remove cuisines with < 50 recipes.

# get list of cuisines to keep
recipes_counts = recipes["cuisine"].value_counts()
cuisines_indices = recipes_counts > 50
​
cuisines_to_keep = list(np.array(recipes_counts.index.values)[np.array(cuisines_indices)])
rows_before = recipes.shape[0] # number of rows of original dataframe
print("Number of rows of original dataframe is {}.".format(rows_before))
​
recipes = recipes.loc[recipes['cuisine'].isin(cuisines_to_keep)]
​
rows_after = recipes.shape[0] # number of rows of processed dataframe
print("Number of rows of processed dataframe is {}.".format(rows_after))
​
print("{} rows removed!".format(rows_before - rows_after))
Convert all Yes's to 1's and the No's to 0's

recipes = recipes.replace(to_replace="Yes", value=1)
recipes = recipes.replace(to_replace="No", value=0)
​
> Run the following cell to get the recipes that contain rice and soy and wasabi and seaweed.

recipes.head()
check_recipes = recipes.loc[
    (recipes["rice"] == 1) &
    (recipes["soy_sauce"] == 1) &
    (recipes["wasabi"] == 1) &
    (recipes["seaweed"] == 1)
]
​
check_recipes

> Let's count the ingredients across all recipes.

# sum each column
ing = recipes.iloc[:, 1:].sum(axis=0)
# define each column as a pandas series
ingredient = pd.Series(ing.index.values, index = np.arange(len(ing)))
count = pd.Series(list(ing), index = np.arange(len(ing)))
​
# create the dataframe
ing_df = pd.DataFrame(dict(ingredient = ingredient, count = count))
ing_df = ing_df[["ingredient", "count"]]
print(ing_df.to_string())


> Now we have a dataframe of ingredients and their total counts across all recipes. Let's sort this dataframe in descending order.

ing_df.sort_values(["count"], ascending=False, inplace=True)
ing_df.reset_index(inplace=True, drop=True)
​
print(ing_df)
          ingredient  count
0                egg  21025
1              wheat  20781
2             butter  20719
3              onion  18080
4             garlic  17353
..               ...    ...
378   strawberry_jam      1
379  sturgeon_caviar      1
380      kaffir_lime      1
381            beech      1
382           durian      0

[383 rows x 2 columns]
