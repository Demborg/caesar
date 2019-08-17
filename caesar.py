from argparse import ArgumentParser

AB = 'abcdefghijklmnopqrstuvxyzåäö'
maping = {}
for i, c in enumerate(AB):
    maping[i] = c
    maping[c] = i
    
def parse_args():
    parser = ArgumentParser()
    parser.add_argument('message', type=str, help='message to encrypt')
    parser.add_argument('--initial_offset', type=int, help='offset for first char in message', default=1)
    parser.add_argument('--offset_update', type=str, help='method for updating the offset', default='none')
    return parser.parse_args()

def no_update(offset, prev_char):
    return offset

def incr_update(offset, prev_char):
    return offset + 1

def rec_update(offset, prev_char):
    return offset + maping[prev_char]

def main():
    args = parse_args()
    message = args.message.lower()
    offset = args.initial_offset
    update = {
            'none': no_update,
            'increment': incr_update,
            'recursive': rec_update
            }.get(args.offset_update, no_update)

    encrypted = ''
    for c in message:
        if c in AB:
            v = maping[c] + offset
            v = v % len(AB)
            encrypted += maping[v]
            offset = update(offset, c)
        else:
            encrypted += c

    print(encrypted)
    

if __name__ == '__main__':
    main()
