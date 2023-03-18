import "./App.css";
import { Routes, Route } from "react-router-dom";
import { ColorModeContext, useMode } from "./theme";

import Sidenav from "./components/Sidenav";
import Topbar from "./components/Topbar";

import { CssBaseline, ThemeProvider } from "@mui/material";
import { useState } from "react";
import Dashboard from "./pages/dashboard/Dashboard";
import BarChart from "./components/BarChart";
import LineChart from "./components/LineChart";

function App() {
  const [theme, colorMode] = useMode();
  const [isSidebar, setIsSidebar] = useState(true);

  return (
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <div className="app">
          <Sidenav isSidebar={isSidebar} />
          <main className="content">
            <Topbar setIsSidebar={setIsSidebar} />
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/bar" element={<BarChart />} />
              <Route path="/line" element={<LineChart />} />
            </Routes>
          </main>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
  );
}

export default App;
