import React from 'react';
import styled from 'styled-components';
import BohrModel from './BohrModel';

const DetailsContainer = styled.div`
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  width: 80%;
  max-width: 800px;
  background-color: #1e1e1e;
  border-radius: 10px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
  padding: 20px;
  display: flex;
  flex-direction: row;
  z-index: 100;
  animation: fadeIn 0.3s ease-in-out;
  
  @keyframes fadeIn {
    from { opacity: 0; transform: translate(-50%, 20px); }
    to { opacity: 1; transform: translate(-50%, 0); }
  }
  
  @media (max-width: 768px) {
    flex-direction: column;
    align-items: center;
  }
`;

const InfoSection = styled.div`
  flex: 1;
  padding-right: 20px;
  
  @media (max-width: 768px) {
    padding-right: 0;
    padding-bottom: 20px;
  }
`;

const VisualSection = styled.div`
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
`;

const ElementHeader = styled.div`
  display: flex;
  align-items: center;
  margin-bottom: 15px;
`;

const ElementSymbol = styled.div`
  font-size: 48px;
  font-weight: bold;
  margin-right: 15px;
  color: #61dafb;
`;

const ElementName = styled.div`
  display: flex;
  flex-direction: column;
`;

const Name = styled.div`
  font-size: 24px;
  font-weight: bold;
`;

const AtomicNumber = styled.div`
  font-size: 16px;
  color: #aaa;
`;

const InfoGrid = styled.div`
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 8px;
  margin-bottom: 15px;
`;

const Label = styled.div`
  font-weight: bold;
  color: #aaa;
`;

const Value = styled.div`
  color: #fff;
`;

const Description = styled.div`
  margin-top: 15px;
  line-height: 1.5;
  color: #ddd;
`;

const ElementDetails = ({ element }) => {
  return (
    <DetailsContainer>
      <InfoSection>
        <ElementHeader>
          <ElementSymbol>{element.symbol}</ElementSymbol>
          <ElementName>
            <Name>{element.name}</Name>
            <AtomicNumber>Atomic Number: {element.atomic_number}</AtomicNumber>
          </ElementName>
        </ElementHeader>
        
        <InfoGrid>
          <Label>Atomic Mass:</Label>
          <Value>{element.atomic_mass} u</Value>
          
          <Label>Category:</Label>
          <Value>{element.category.charAt(0).toUpperCase() + element.category.slice(1)}</Value>
          
          <Label>Electron Configuration:</Label>
          <Value>{element.electron_configuration}</Value>
        </InfoGrid>
        
        <Description>{element.description}</Description>
      </InfoSection>
      
      <VisualSection>
        <BohrModel element={element} />
      </VisualSection>
    </DetailsContainer>
  );
};

export default ElementDetails;
