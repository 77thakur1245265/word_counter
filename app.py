from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/count_words_and_characters', methods=['POST'])
def count_words_and_characters():
    file = request.files['file']

    try:
        # Read the contents of the text file
        text_content = file.read().decode('utf-8')

        # Count words
        words = text_content.split()
        word_count = len(words)

        # Count characters (including spaces)
        char_count = len(text_content)

        # Count digits
        digit_count = sum(c.isdigit() for c in text_content)

        return jsonify({'word_count': word_count, 'char_count': char_count, 'digit_count': digit_count})

    except Exception as e:
        return jsonify({'error': f'Text file processing error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
