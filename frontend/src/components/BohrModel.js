import React, { useRef, useEffect } from 'react';
import styled from 'styled-components';

const CanvasContainer = styled.div`
  width: 300px;
  height: 300px;
`;

const BohrCanvas = styled.canvas`
  width: 100%;
  height: 100%;
`;

const BohrModel = ({ element }) => {
  const canvasRef = useRef(null);
  
  useEffect(() => {
    if (!canvasRef.current || !element) return;
    
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const { width, height } = canvas;
    
    // Set canvas resolution for high DPI displays
    const dpr = window.devicePixelRatio || 1;
    canvas.width = width * dpr;
    canvas.height = height * dpr;
    ctx.scale(dpr, dpr);
    
    // Clear canvas
    ctx.clearRect(0, 0, width, height);
    
    // Center of the atom
    const centerX = width / 2;
    const centerY = height / 2;
    
    // Draw nucleus
    ctx.beginPath();
    ctx.arc(centerX, centerY, 15, 0, Math.PI * 2);
    ctx.fillStyle = '#ff5722';
    ctx.fill();
    ctx.strokeStyle = '#ff8a65';
    ctx.lineWidth = 2;
    ctx.stroke();
    
    // Draw electron shells
    const shells = element.electron_shells;
    const maxShells = shells.length;
    const maxRadius = Math.min(width, height) / 2 - 10;
    const shellSpacing = maxRadius / maxShells;
    
    shells.forEach((electronCount, shellIndex) => {
      const shellRadius = (shellIndex + 1) * shellSpacing;
      
      // Draw shell orbit
      ctx.beginPath();
      ctx.arc(centerX, centerY, shellRadius, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(97, 218, 251, 0.5)';
      ctx.lineWidth = 1;
      ctx.stroke();
      
      // Draw electrons on this shell
      const angleStep = (Math.PI * 2) / electronCount;
      
      for (let i = 0; i < electronCount; i++) {
        const angle = i * angleStep;
        const electronX = centerX + Math.cos(angle) * shellRadius;
        const electronY = centerY + Math.sin(angle) * shellRadius;
        
        // Draw electron
        ctx.beginPath();
        ctx.arc(electronX, electronY, 5, 0, Math.PI * 2);
        ctx.fillStyle = '#61dafb';
        ctx.fill();
        
        // Add glow effect
        const gradient = ctx.createRadialGradient(
          electronX, electronY, 0,
          electronX, electronY, 8
        );
        gradient.addColorStop(0, 'rgba(97, 218, 251, 0.8)');
        gradient.addColorStop(1, 'rgba(97, 218, 251, 0)');
        
        ctx.beginPath();
        ctx.arc(electronX, electronY, 8, 0, Math.PI * 2);
        ctx.fillStyle = gradient;
        ctx.fill();
      }
    });
    
    // Add element symbol in nucleus
    ctx.fillStyle = 'white';
    ctx.font = 'bold 14px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(element.symbol, centerX, centerY);
    
    // Add animation effect (optional)
    let rotation = 0;
    const animate = () => {
      rotation += 0.005;
      
      // Clear canvas
      ctx.clearRect(0, 0, width, height);
      
      // Draw nucleus
      ctx.beginPath();
      ctx.arc(centerX, centerY, 15, 0, Math.PI * 2);
      ctx.fillStyle = '#ff5722';
      ctx.fill();
      ctx.strokeStyle = '#ff8a65';
      ctx.lineWidth = 2;
      ctx.stroke();
      
      // Draw element symbol in nucleus
      ctx.fillStyle = 'white';
      ctx.font = 'bold 14px Arial';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(element.symbol, centerX, centerY);
      
      // Draw electron shells with rotation
      shells.forEach((electronCount, shellIndex) => {
        const shellRadius = (shellIndex + 1) * shellSpacing;
        
        // Draw shell orbit
        ctx.beginPath();
        ctx.arc(centerX, centerY, shellRadius, 0, Math.PI * 2);
        ctx.strokeStyle = 'rgba(97, 218, 251, 0.5)';
        ctx.lineWidth = 1;
        ctx.stroke();
        
        // Draw electrons on this shell with rotation
        const angleStep = (Math.PI * 2) / electronCount;
        const shellRotation = rotation * (maxShells - shellIndex) / 2; // Outer shells rotate faster
        
        for (let i = 0; i < electronCount; i++) {
          const angle = i * angleStep + shellRotation;
          const electronX = centerX + Math.cos(angle) * shellRadius;
          const electronY = centerY + Math.sin(angle) * shellRadius;
          
          // Draw electron
          ctx.beginPath();
          ctx.arc(electronX, electronY, 5, 0, Math.PI * 2);
          ctx.fillStyle = '#61dafb';
          ctx.fill();
          
          // Add glow effect
          const gradient = ctx.createRadialGradient(
            electronX, electronY, 0,
            electronX, electronY, 8
          );
          gradient.addColorStop(0, 'rgba(97, 218, 251, 0.8)');
          gradient.addColorStop(1, 'rgba(97, 218, 251, 0)');
          
          ctx.beginPath();
          ctx.arc(electronX, electronY, 8, 0, Math.PI * 2);
          ctx.fillStyle = gradient;
          ctx.fill();
        }
      });
      
      requestAnimationFrame(animate);
    };
    
    const animationId = requestAnimationFrame(animate);
    
    // Cleanup animation on unmount
    return () => {
      cancelAnimationFrame(animationId);
    };
  }, [element]);
  
  return (
    <CanvasContainer>
      <BohrCanvas ref={canvasRef} width="300" height="300" />
    </CanvasContainer>
  );
};

export default BohrModel;
