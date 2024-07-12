// @ts-ignore: React is declared but its value is never read
import React, { useState } from 'react';

const Settings = () => {
    const [openAIKey, setOpenAIKey] = useState('');
    const [openAIBaseURL, setOpenAIBaseURL] = useState('');
    const [anthropicKey, setAnthropicKey] = useState('');

    return (
        <div className="settings-container">
            <h2>Settings</h2>
            <div className="settings-section">
                <h3>DALL-E Placeholder Image Generation</h3>
                <p>More fun with it but if you want to save money, turn it off.</p>
            </div>
            <div className="settings-section">
                <h3>OpenAI API key</h3>
                <p>Only stored in your browser. Never stored on servers. Overrides your .env config.</p>
                <input
                    type="text"
                    value={openAIKey}
                    onChange={(e) => setOpenAIKey(e.target.value)}
                    placeholder="OpenAI API key"
                />
            </div>
            <div className="settings-section">
                <h3>OpenAI Base URL (optional)</h3>
                <p>Replace with a proxy URL if you don't want to use the default.</p>
                <input
                    type="text"
                    value={openAIBaseURL}
                    onChange={(e) => setOpenAIBaseURL(e.target.value)}
                    placeholder="OpenAI Base URL"
                />
            </div>
            <div className="settings-section">
                <h3>Anthropic API key</h3>
                <p>Only stored in your browser. Never stored on servers. Overrides your .env config.</p>
                <input
                    type="text"
                    value={anthropicKey}
                    onChange={(e) => setAnthropicKey(e.target.value)}
                    placeholder="Anthropic API key"
                />
            </div>
            <div className="settings-section">
                <h3>Screenshot by URL Config</h3>
                {/* Añade la configuración necesaria para Screenshot by URL */}
            </div>
            <div className="settings-section">
                <h3>Theme Settings</h3>
                {/* Añade la configuración necesaria para Theme Settings */}
            </div>
        </div>
    );
};

export default Settings;
