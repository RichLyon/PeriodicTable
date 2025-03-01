import React from 'react';
import styled from 'styled-components';
import ElementCell from './ElementCell';

const TableContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 30px;
  max-width: 100%;
  overflow-x: auto;
`;

const TableRow = styled.div`
  display: flex;
  margin-bottom: 4px;
`;

const EmptyCell = styled.div`
  width: 70px;
  height: 70px;
  margin: 2px;
`;

const PeriodicTable = ({ elements, categories, layout, onElementHover, onElementLeave }) => {
  // Create a map of elements by atomic number for easy lookup
  const elementsMap = elements.reduce((acc, element) => {
    acc[element.atomic_number] = element;
    return acc;
  }, {});

  return (
    <TableContainer>
      {layout.map((row, rowIndex) => (
        <TableRow key={`row-${rowIndex}`}>
          {row.map((atomicNumber, colIndex) => {
            if (atomicNumber === 0) {
              return <EmptyCell key={`empty-${rowIndex}-${colIndex}`} />;
            }
            
            const element = elementsMap[atomicNumber];
            if (!element) {
              return <EmptyCell key={`unknown-${rowIndex}-${colIndex}`} />;
            }
            
            return (
              <ElementCell
                key={`element-${element.atomic_number}`}
                element={element}
                color={categories[element.category]}
                onMouseEnter={() => onElementHover(element)}
                onMouseLeave={onElementLeave}
              />
            );
          })}
        </TableRow>
      ))}
    </TableContainer>
  );
};

export default PeriodicTable;
