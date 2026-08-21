import overpy

class GeoModule:
    def __init__(self):
        self.api = overpy.Overpass()

    def load_city_skeleton(self, bbox):
        """
        Изтегля мрежа от улици и контури на сгради от OpenStreetMap за подаден BBox:
        (min_lat, min_lon, max_lat, max_lon)
        """
        query = f"""
        [out:json][timeout:30];
        (
          way["highway"]({bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]});
          way["building"]({bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]});
        );
        out body;
        >;
        out skel qt;
        """
        try:
            result = self.api.query(query)
            parsed_data = {"roads": [], "buildings": []}
            
            for way in result.ways:
                nodes = [(float(node.lat), float(node.lon)) for node in way.nodes]
                if "highway" in way.tags:
                    parsed_data["roads"].append(nodes)
                elif "building" in way.tags:
                    parsed_data["buildings"].append(nodes)
                    
            return parsed_data
        except Exception as e:
            print(f"GeoModule Execution Error: {e}")
            return None
