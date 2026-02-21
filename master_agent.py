from typing import Dict, Any
import logging
from datetime import datetime
from monitoring_module import MonitoringModule
from knowledge_base import KnowledgeBase
from data_collection_module import DataCollectionModule
from analysis_module import AnalysisModule
from feedback_loop import FeedbackLoop

class MasterAgent:
    def __init__(self):
        self.monitoring = MonitoringModule()
        self.knowledge_base = KnowledgeBase()
        self.data_collector = DataCollectionModule()
        self.analyzer = AnalysisModule()
        self.feedback_loop = FeedbackLoop()
        
        # Initialize logging
        logging.basicConfig(
            filename='master_agent.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def process_data(self) -> Dict[str, Any]:
        """
        Collects data from various sources, analyzes it, and generates feedback.
        Returns a dictionary with the processed results.
        """
        try:
            # Step 1: Collect data
            collected_data = self.data_collector.collect_data()
            
            # Log successful collection
            logging.info(f"Data collected at {datetime.now()}")
            
            # Step 2: Analyze data
            analysis_results = self.analyzer.analyze(collected_data)
            
            # Log successful analysis
            logging.info(f"Analysis completed at {datetime.now()}")
            
            # Step 3: Generate feedback
            feedback = self.feedback_loop.generate_feedback(analysis_results)
            
            # Log feedback generation
            logging.info(f"Feedback generated at {datetime.now()}")

            return {
                'status': 'success',
                'data': analysis_results,
                'feedback': feedback
            }

        except Exception as e:
            logging.error(f"Error in processing data: {str(e)}")
            self.monitoring.alert("Critical error in MasterAgent.process_data", str(e))
            raise

    def learn(self, feedback_data: Dict[str, Any]) -> None:
        """
        Implements closed-loop learning by updating the knowledge base and optimizing processes.
        """
        try:
            # Store feedback in knowledge base
            self.knowledge_base.update('master_agent_learn', feedback_data)
            
            # Optimize internal processes based on feedback
            self.analyzer.optimize_models(feedback_data)
            
            logging.info(f"Learning completed with new data at {datetime.now()}")
            
        except Exception as e:
            logging.error(f"Error in learning process: {str(e)}")
            self.monitoring.alert("Critical error in MasterAgent.learn", str(e))
            raise

    def run(self) -> None:
        """
        Main execution loop for the Master Agent.
        Continuously processes data and learns from feedback.
        """
        try:
            while True:
                # Process data
                result = self.process_data()
                
                # Generate insights
                insights = self.analyzer.generate_insights(result['data'])
                
                # Provide feedback
                self.learn({
                    'timestamp': datetime.now().isoformat(),
                    'insights': insights,
                    'metrics': result['feedback']
                })
                
                # Sleep for a short period before next iteration
                sleep(60)  # Sleep for 1 minute
                
        except KeyboardInterrupt:
            logging.info("Master Agent shutting down gracefully")
            self.monitoring.shutdown()
            exit(0)