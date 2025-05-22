class PropertyListing:
    def __init__(self, description, location, price, features, link):
        self.description = description
        self.location = location
        self.price = price
        self.features = features
        self.link = link

    def __repr__(self):
        return (f"<PropertyListing(description={self.description!r}, "
                f"location={self.location!r}, price={self.price!r})>")
