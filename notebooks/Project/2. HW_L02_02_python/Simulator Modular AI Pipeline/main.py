from pipeline import ( 
    DataLoader, 
    Preprocessor, 
    Analyzer, 
    ReportGenerator, 
    AIPipeline)

if __name__ == "__main__":
       # --- Component Definitions --- 
    loader = DataLoader() 
    preprocessor = Preprocessor() 
    basic_analyzer = Analyzer() 
    reporter = ReportGenerator() 
 
    input_filepath =r"C:\Mohsen Folder\Ai Bootcamp\Ai Bootcamp\notebooks\Project\2. HW_L02_02_python\Simulator Modular AI Pipeline"


    # --- Pipeline  --- 
    print("\n---------------- Running Pipeline ----------") 
    basic_pipeline = AIPipeline(loader, preprocessor, basic_analyzer) 
    basic_results = basic_pipeline.run(input_filepath) 
    reporter.print_to_console(basic_results)
