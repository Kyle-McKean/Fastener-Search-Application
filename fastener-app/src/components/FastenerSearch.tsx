import React, { useState } from "react";

type FastenerResult = {
  code: string;
  description: string;
  location?: string;
};

const FastenerSearch: React.FC = () => {
  const [searchValue, setSearchValue] = useState<string>("");
  const [result, setResult] = useState<FastenerResult | null>(null);
  const [error, setError] = useState<string>("");

  const handleSearch = async () => {
    setError("");
    setResult(null);

    if (!searchValue.trim()) {
      setError("Please enter a fastener code.");
      return;
    }

    try {
      const response = await fetch(
        `http://127.0.0.1:5000/api/fasteners/${searchValue}`
      );

      if (!response.ok) {
        throw new Error("Fastener not found.");
      }

      const data: FastenerResult = await response.json();
      setResult(data);
    } catch (err) {
      setError("Could not find that fastener.");
    }
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>Fasteners Search</h2>

      <input
        type="text"
        placeholder="Enter 3-letter code..."
        value={searchValue}
        onChange={(e) => setSearchValue(e.target.value.toUpperCase())}
        style={styles.input}
      />

      <button onClick={handleSearch} style={styles.button}>
        Search
      </button>

      <div style={styles.resultBox}>
        {error && <p style={styles.error}>{error}</p>}

        {result && (
          <>
            <p><strong>Code:</strong> {result.code}</p>
            <p><strong>Description:</strong> {result.description}</p>
            {result.location && (
              <p><strong>Location:</strong> {result.location}</p>
            )}
          </>
        )}
      </div>
    </div>
  );
};

export default FastenerSearch;

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    width: "350px",
    minHeight: "350px",
    border: "2px solid #ccc",
    borderRadius: "10px",
    padding: "20px",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    backgroundColor: "#f9f9f9",
  },
  title: {
    marginBottom: "20px",
  },
  input: {
    width: "100%",
    padding: "10px",
    fontSize: "16px",
    borderRadius: "5px",
    border: "1px solid #ccc",
    marginBottom: "12px",
  },
  button: {
    width: "100%",
    padding: "10px",
    fontSize: "16px",
    borderRadius: "5px",
    border: "none",
    cursor: "pointer",
    backgroundColor: "#f96302",
    color: "white",
    fontWeight: "bold",
  },
  resultBox: {
    marginTop: "20px",
    width: "100%",
    textAlign: "left",
  },
  error: {
    color: "red",
  },
};