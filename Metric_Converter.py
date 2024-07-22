class Metric_Converter:
    @staticmethod
    def Kilometrs_to_Miles(Kilometr):
        return Kilometr / 1.609
    
    @staticmethod
    def Miles_to_Kilometrs(Mile):
        return Mile * 1.609

    @staticmethod
    def Galons_to_Liters(Galon):
        return Galon * 3.785
    
    @staticmethod 
    def Liters_to_Galons(Liter):
        return Liter / 3.785

if __name__ == "__main__":
    print(Metric_Converter.Kilometrs_to_Miles(42.195))
    print(Metric_Converter.Miles_to_Kilometrs(26.2195))
    print(Metric_Converter.Galons_to_Liters(5.5))
    print(Metric_Converter.Liters_to_Galons(20.8194))