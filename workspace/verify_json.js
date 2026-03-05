const fs = require('fs');
try {
    const content = fs.readFileSync('/root/.openclaw/openclaw.json', 'utf-8');
    JSON.parse(content);
    console.log('JSON validation passed.');
} catch (e) {
    console.error('JSON validation failed', e);
    process.exit(1);
}
