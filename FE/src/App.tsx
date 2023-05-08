import React from "react";
import "./App.css";
import { Route, Routes } from "react-router-dom";
import EditCoursesPage from "./components/pages/EditCoursesPage";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path={"/"} element={<EditCoursesPage />} />
      </Routes>
    </div>
  );
}

export default App;
