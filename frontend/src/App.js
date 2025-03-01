import React, { useState, useEffect } from 'react';
import axios from 'axios';
import styled from 'styled-components';
import PeriodicTable from './components/PeriodicTable';
import ElementDetails from './components/ElementDetails';

const AppContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
  padding: 20px;
  background-color: #121212;
  color: #ffffff;
`;

const Title = styled.h1`
  font-size: 2.5rem;
  margin-bottom: 20px;
  text-align: center;
  color: #61dafb;
  text-shadow: 0 0 10px rgba(97, 218, 251, 0.5);
`;

const LoadingMessage = styled.div`
  font-size: 1.5rem;
  margin-top: 50px;
  color: #61dafb;
`;

const ErrorMessage = styled.div`
  font-size: 1.5rem;
  margin-top: 50px;
  color: #ff6b6b;
`;

function App() {
  const [elementsData, setElementsData] = useState(null);
  const [categories, setCategories] = useState({});
  const [layout, setLayout] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedElement, setSelectedElement] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/elements');
        setElementsData(response.data.elements);
        setCategories(response.data.categories);
        setLayout(response.data.layout);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching data:', err);
        setError('Failed to load periodic table data. Please try again later.');
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const handleElementHover = (element) => {
    setSelectedElement(element);
  };

  const handleElementLeave = () => {
    setSelectedElement(null);
  };

  if (loading) {
    return (
      <AppContainer>
        <Title>Interactive Periodic Table</Title>
        <LoadingMessage>Loading periodic table data...</LoadingMessage>
      </AppContainer>
    );
  }

  if (error) {
    return (
      <AppContainer>
        <Title>Interactive Periodic Table</Title>
        <ErrorMessage>{error}</ErrorMessage>
      </AppContainer>
    );
  }

  return (
    <AppContainer>
      <Title>Interactive Periodic Table</Title>
      <PeriodicTable 
        elements={elementsData} 
        categories={categories}
        layout={layout}
        onElementHover={handleElementHover}
        onElementLeave={handleElementLeave}
      />
      {selectedElement && <ElementDetails element={selectedElement} />}
    </AppContainer>
  );
}

export default App;
