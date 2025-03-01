import React from 'react';
import styled from 'styled-components';

const Cell = styled.div`
  width: 70px;
  height: 70px;
  margin: 2px;
  padding: 5px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: ${props => props.color || '#333'};
  border-radius: 4px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease;
  cursor: pointer;
  
  &:hover {
    transform: scale(1.05);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
    z-index: 10;
  }
`;

const AtomicNumber = styled.div`
  font-size: 10px;
  text-align: left;
  color: rgba(255, 255, 255, 0.8);
`;

const Symbol = styled.div`
  font-size: 24px;
  font-weight: bold;
  text-align: center;
  margin: auto 0;
`;

const Name = styled.div`
  font-size: 8px;
  text-align: center;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
`;

const Mass = styled.div`
  font-size: 8px;
  text-align: right;
  color: rgba(255, 255, 255, 0.8);
`;

const ElementCell = ({ element, color, onMouseEnter, onMouseLeave }) => {
  return (
    <Cell 
      color={color}
      onMouseEnter={onMouseEnter}
      onMouseLeave={onMouseLeave}
    >
      <AtomicNumber>{element.atomic_number}</AtomicNumber>
      <Symbol>{element.symbol}</Symbol>
      <Name>{element.name}</Name>
      <Mass>{element.atomic_mass.toFixed(2)}</Mass>
    </Cell>
  );
};

export default ElementCell;
