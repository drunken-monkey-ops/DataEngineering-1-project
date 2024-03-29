  db.tweet.aggregate([
    {
        $match: {
            "text": {
                $regex: /han|hon|den|det|denna|denne|hen/i
            }
        }
    },
    {
        $project: {
            _id: 0,
            pronouns: {
                $split: ["$text", " "]
            }
        }
    },
    {
        $unwind: "$pronouns"
    },
    {
        $match: {
            "pronouns": {
                $in: ["han", "hon", "den", "det", "denna", "denne", "hen"]
            }
        }
    },
    {
        $group: {
            _id: {
                $toLower: "$pronouns"
            },
            count: {
                $sum: 1
            }
        }
    },
    {
        $project: {
            _id: 0,
            pronoun: "$_id",
            count: 1
        }
    }
])
