import React from 'react';
import Button from 'components/atoms/button/Button';
import {StyledTabGroup} from './StyledTabGroup';
import { useNavigate } from 'react-router-dom';
import { paths } from 'components/routes/routes';


const TabGroup = () => {

  const navigate = useNavigate();

  return (
    <StyledTabGroup>
      <Button 
        title='Plan Holiday' 
        color='secondary' 
        onClick={() => navigate(paths.home)}
      />
      <Button 
        title='Departures' 
        color='secondary' 
        onClick={() => navigate(paths.flights)}
      />
      <Button
        title='See Trends' 
        color='secondary' 
        onClick={() => navigate(paths.trends)}
      />
    </StyledTabGroup>
  )
}

export default TabGroup
