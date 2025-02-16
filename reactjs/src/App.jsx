import { HashRouter, Route, Routes } from 'react-router-dom';

import UploadData from "./pages/UploadData";
import ActiveCampaigns from './pages/ActiveCampaigns';

function App() {

  return (
    <HashRouter>
      <Routes>
        <Route
          path="/uploaddataform"
          element={<UploadData />} />
        <Route
          path="/"
          element={<ActiveCampaigns />} />
      </Routes>
    </HashRouter>
  )
}

export default App
