def transaction_data_to_features(data):
        data = [
            data["avg_amount_days"],
            data["amount"],
            1 if data["is_declined"] else 0,
            data["number_declined_days"],
            1 if data["foreign_transaction"] else 0,
            1 if data["high_risk_countries"] else 0,
            data["daily_chbk_avg_amt"],
            data["sixm_avg_chbk_amt"],
            data["sixm_chbk_freq"],
        ]
        return data