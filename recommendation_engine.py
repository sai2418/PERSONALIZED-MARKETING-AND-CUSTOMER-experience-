import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import OneHotEncoder
import numpy as np

class RecommendationEngine:
    def __init__(self, user_data, product_data):
        self.user_data = user_data
        self.product_data = product_data

    def get_recommendations(self, user_id):
        user_row = self.user_data[self.user_data['user_id'] == int(user_id)]

        if user_row.empty:
            print(f"No user found with user_id: {user_id}")
            return []

        browsing_cat = user_row.iloc[0]['browsing_category']
        purchase_cat = user_row.iloc[0]['purchase_category']

        recommendations = self.product_data[
            (self.product_data['category'] == browsing_cat) |
            (self.product_data['category'] == purchase_cat)
        ]

        return recommendations['name'].tolist()
