import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    temp = views[views['author_id'] == views['viewer_id']]
    temp = temp.sort_values("author_id")
    temp = temp.drop_duplicates(subset=['author_id'])
    return temp[['author_id']].rename(columns={'author_id':'id'})
