// Initialize Vue app
const app = Vue.createApp({
    data() {
        return {
            // Input values
            rawPrompt: '',
            selectedTone: 'neutral',
            selectedLength: 'medium',
            selectedFormat: 'paragraph',
            selectedModel: 'EleutherAI/gpt-neo-125M',
            selectedModelName: 'GPT-Neo (125M)',
            selectedRole: 'general',
            charLimit: 500,
            variantsNumber: 1,
            
            // UI state
            isProcessing: false,
            optimizedPrompts: [],
            errorMessage: '',
            
            // Options for dropdowns
            tones: [
                { label: 'Neutral', value: 'neutral' },
                { label: 'Formal', value: 'formal' },
                { label: 'Informal', value: 'informal' },
                { label: 'Friendly', value: 'friendly' },
                { label: 'Professional', value: 'professional' },
                { label: 'Academic', value: 'academic' },
                { label: 'Creative', value: 'creative' },
                { label: 'Technical', value: 'technical' }
            ],
            lengths: [
                { label: 'Very Short', value: 'veryshort' },
                { label: 'Short', value: 'short' },
                { label: 'Medium', value: 'medium' },
                { label: 'Long', value: 'long' },
                { label: 'Very Long', value: 'verylong' }
            ],
            formats: [
                { label: 'Paragraph', value: 'paragraph' },
                { label: 'Bullet Points', value: 'bullets' },
                { label: 'Numbered List', value: 'numbered' },
                { label: 'Questions', value: 'questions' },
                { label: 'Conversation', value: 'conversation' },
                { label: 'Code', value: 'code' }
            ],
            roles: [
                { label: 'General', value: 'general' },
                { label: 'Developer', value: 'developer' },
                { label: 'Teacher', value: 'teacher' },
                { label: 'Business Analyst', value: 'business' },
                { label: 'Creative Writer', value: 'writer' },
                { label: 'Academic', value: 'academic' },
                { label: 'Marketer', value: 'marketer' },
                { label: 'Technical Expert', value: 'technical' }
            ],
            models: []
        };
    },
    
    mounted() {
        // Fetch available models on page load
        this.fetchModels();
    },
    
    methods: {
        async fetchModels() {
            try {
                const response = await fetch('/api/models');
                const data = await response.json();
                this.models = data;
                
                // Update the model name when models are loaded
                this.updateModelName();
            } catch (error) {
                console.error('Error fetching models:', error);
            }
        },
        
        updateModelName() {
            // Find the name of the currently selected model
            const model = this.models.find(m => m.id === this.selectedModel);
            if (model) {
                this.selectedModelName = model.name;
            }
        },
        
        async onModelChange() {
            this.updateModelName();
            
            // Notify the backend of the model change
            try {
                this.isProcessing = true;
                const response = await fetch('/api/change-model', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        model: this.selectedModel
                    })
                });
                
                const data = await response.json();
                if (data.error) {
                    console.error('Error changing model:', data.error);
                    alert('Error changing model: ' + data.error);
                }
            } catch (error) {
                console.error('Error changing model:', error);
                alert('Error changing model: ' + error.message);
            } finally {
                this.isProcessing = false;
            }
        },
        
        async optimizePrompt() {
            if (!this.rawPrompt.trim()) {
                alert('Please enter a prompt to optimize');
                return;
            }
            
            this.isProcessing = true;
            this.optimizedPrompts = [];
            this.errorMessage = '';
            
            try {
                const response = await fetch('/api/optimize-prompt', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        prompt: this.rawPrompt,
                        tone: this.selectedTone,
                        length: this.selectedLength,
                        format: this.selectedFormat,
                        model: this.selectedModel,
                        role: this.selectedRole,
                        charLimit: this.charLimit,
                        variants: this.variantsNumber
                    })
                });
                
                const data = await response.json();
                
                if (data.error) {
                    this.errorMessage = data.error;
                    alert('Error optimizing prompt: ' + data.error);
                } else {
                    this.optimizedPrompts = data.results;
                }
            } catch (error) {
                console.error('Error optimizing prompt:', error);
                this.errorMessage = error.message;
                alert('Error optimizing prompt: ' + error.message);
            } finally {
                this.isProcessing = false;
            }
        },
        
        copyToClipboard(text) {
            navigator.clipboard.writeText(text)
                .then(() => {
                    // Show a temporary "Copied!" tooltip or notification
                    // For simplicity, we're using alert here, but you could create a nicer UI notification
                    alert('Copied to clipboard!');
                })
                .catch(err => {
                    console.error('Failed to copy text: ', err);
                    alert('Failed to copy: ' + err.message);
                });
        }
    }
});

// Mount the Vue app
app.mount('#app');