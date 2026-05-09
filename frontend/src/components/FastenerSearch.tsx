import React, { useState } from "react";
import "../css/FastenerSearch.css";

// Defines the structure of the fastener search data returned
type FastenerResult = {
  code: string;
  material: string;
  size: string;
  length: string;
  name: string;
};

const capitalizeWords = (value: string): string => {
  if (!value) return "";

  return value
    .split(" ")
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
};

const sizeFormat = (value: string): string => {
  if (!value) return "";
  return `${value}"`;
}

const lengthFormat = (value: string): string => {
  if (!value) return "";
  return `x ${value}"`;
}

// React component to handle the search functionality for fasteners
const FastenerSearch: React.FC = () => {

  

  // search value for the fastener input
  const [searchValue, setSearchValue] = useState<string>("");
  
  // result of the search, initially null
  const [result, setResult] = useState<FastenerResult | null>(null);
  
  // error message to display if the search fails
  const [error, setError] = useState<string>("");

  // function to handle the faster search feature
  const handleSearch = async () => {
    // Resets error and result before performing a new search
    setError("");
    setResult(null);

    // Checks if the search value is valid (not null, empty, and 3 characters long)
    if (!searchValue.trim() || searchValue.length !== 3 || !/^[A-Z]+$/.test(searchValue)) {
      setError("Invalid code. Please enter a 3-letter fastener code.");
      return;
    }

            console.log("APIURL:", `${import.meta.env.VITE_API_URL}/items/${searchValue}`);


    // Attempts to fetch the fastener data from the backend API
    // try: fetches the data and updates the result state if successful
    // catch: sets an error message if the fetch fails (e.g., fastener not found)
    try {

      // response from the backend
      const response = await fetch(
        // Uncomment for local testing
        `${import.meta.env.VITE_API_URL}/items/${searchValue}`
        
      );

      // checks if the response does not contain an error
      if (!response.ok) {
        throw new Error("Fastener not found.");
      }

      // parses the response data as JSON
      const data: FastenerResult = await response.json();
      setResult(data);
    
    } catch (err) {
      console.error(err);
      setError("Could not find that fastener.");
    }
  };

  return (
    <div className = "container">
      <h1 className = "title">Fastener Search</h1>
      <h2 className = "title">Enter a 3-letter fastener code to search</h2>
      

      
      
      
  <form
      onSubmit={(e) => {
        e.preventDefault(); // prevents page refresh
        handleSearch();
  }}>
  <input
    type="text"
    placeholder="Enter Code"
    value={searchValue}
    onChange={(e) => setSearchValue(e.target.value.toUpperCase())}
    maxLength={3}
    className="input"
  />

    <button type="submit" className="button">
      Search
    </button>
  </form>

      <div className = "resultBox">
        {error && <p className = "error">{error}</p>}

        {result && (
          <>
            <p><strong>Code:</strong> {result.code}</p>
            <p>{capitalizeWords(result.material)} {sizeFormat(result.size)} {lengthFormat(result.length)} {capitalizeWords(result.name)} </p>
          </>
        )}
      </div>
    </div>
  );
};

export default FastenerSearch;
