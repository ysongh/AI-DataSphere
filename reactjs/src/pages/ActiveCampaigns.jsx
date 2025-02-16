import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Clock } from 'lucide-react';

const ActiveCampaigns = () => {
  const navigate = useNavigate();

  const [campaigns] = useState([
    {
      id: 1,
      title: "Image Classification Dataset",
      description: "Collect labeled images for ML model training",
      deadline: "2025-03-15",
      submissionsCount: 45,
      requiredSubmissions: 100,
      category: "image",
      status: "active"
    },
    {
      id: 2,
      title: "Text Sentiment Analysis",
      description: "Gather sentiment-labeled text samples",
      deadline: "2025-03-20",
      submissionsCount: 120,
      requiredSubmissions: 200,
      category: "text",
      status: "active"
    },
    {
      id: 3,
      title: "Voice Command Dataset",
      description: "Record voice commands for AI assistant",
      deadline: "2025-03-25",
      submissionsCount: 30,
      requiredSubmissions: 150,
      category: "audio",
      status: "active"
    }
  ]);

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <h1 className="text-2xl font-bold text-gray-900 mb-3">Active Campaigns</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {campaigns.map(campaign => (
            <div 
              key={campaign.id}
              className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-200"
            >
              <div className="p-6">
                <div className="flex justify-between items-start mb-4">
                  <h3 className="text-lg font-semibold text-gray-900">{campaign.title}</h3>
                  <span className="px-2 py-1 text-xs font-semibold rounded-full bg-green-100 text-green-800">
                    {campaign.category}
                  </span>
                </div>
                
                <p className="text-gray-600 mb-4">{campaign.description}</p>
                
                <div className="space-y-3">
                  <div className="flex items-center text-sm text-gray-500">
                    <Clock className="h-4 w-4 mr-2" />
                    <span>Deadline: {campaign.deadline}</span>
                  </div>
                  
                  <div className="bg-gray-100 rounded-full h-2 mb-4">
                    <div 
                      className="bg-blue-500 rounded-full h-2"
                      style={{ width: `${(campaign.submissionsCount / campaign.requiredSubmissions) * 100}%` }}
                    />
                  </div>
                  
                  <div className="text-sm text-gray-500 text-center">
                    {campaign.submissionsCount} / {campaign.requiredSubmissions} submissions
                  </div>
                </div>
                
                <button
                  onClick={() => navigate("/uploaddataform")}
                  className="mt-4 w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-md cursor-pointer transition duration-150 ease-in-out disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  Participate
                </button>
              </div>
            </div>
          ))}
        </div>
        
        {campaigns.length === 0 && (
          <div className="text-center py-12">
            <p className="text-gray-500">No campaigns found matching your criteria.</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default ActiveCampaigns;