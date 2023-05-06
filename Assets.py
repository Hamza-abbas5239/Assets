class Asset:
    def __init__(self, asset_id, asset_name, location, condition, maintenance_history):
        self.asset_id = asset_id
        self.asset_name = asset_name
        self.location = location
        self.condition = condition
        self.maintenance_history = maintenance_history
        
    def update_location(self, new_location):
        self.location = new_location
        
    def update_condition(self, new_condition):
        self.condition = new_condition
        
    def add_maintenance_history(self, maintenance_event):
        self.maintenance_history.append(maintenance_event)
        
    def print_asset_details(self):
        print(f'Asset ID: {self.asset_id}')
        print(f'Asset Name: {self.asset_name}')
        print(f'Location: {self.location}')
        print(f'Condition: {self.condition}')
        print(f'Maintenance History: {self.maintenance_history}')


class FixedAsset(Asset):
    def __init__(self, asset_id, asset_name, location, condition, maintenance_history):
        super().__init__(asset_id, asset_name, location, condition, maintenance_history)


class Computer(Asset):
    def __init__(self, asset_id, asset_name, location, condition, maintenance_history, brand, model):
        super().__init__(asset_id, asset_name, location, condition, maintenance_history)
        self.brand = brand
        self.model = model
        
    def print_asset_details(self):
        super().print_asset_details()
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')


class FixedAssetDatabase:
    def __init__(self):
        self.assets = []
        
    def add_asset(self, asset):
        self.assets.append(asset)
        
    def remove_asset(self, asset_id):
        for asset in self.assets:
            if asset.asset_id == asset_id:
                self.assets.remove(asset)
                
    def update_asset_location(self, asset_id, new_location):
        for asset in self.assets:
            if asset.asset_id == asset_id:
                asset.update_location(new_location)
                
    def update_asset_condition(self, asset_id, new_condition):
        for asset in self.assets:
            if asset.asset_id == asset_id:
                asset.update_condition(new_condition)
                
    def add_asset_maintenance_history(self, asset_id, maintenance_event):
        for asset in self.assets:
            if asset.asset_id == asset_id:
                asset.add_maintenance_history(maintenance_event)
                
    def print_all_assets(self):
        for asset in self.assets:
            asset.print_asset_details()


# Example usage:

computer = Computer('C01', 'Desktop', 'Room A', 'Good', ['Cleaned'], 'Dell', 'Optiplex')
database = FixedAssetDatabase()
database.add_asset(computer)
database.print_all_assets() # prints the details of the computer object
